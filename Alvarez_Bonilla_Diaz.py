"""
Proyecto Final: Modelado y control del sistema gastrointestinal - Gastroparesia Diabética

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Integrantes del Equipo y Número de control:
Gabriela Gissele Alvarez Garcia               C22211520
Bonilla Martinez Nayeli                       22212381
Diaz de Leon Bernal David Emiliano            C23211564
Correo institucional: 
C22211520@tectijuana.edu.mx
l22212381@tectijuana.edu.mx
l23211564@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""
# Instalar librerias en consola
#!pip install control
#!pip install slycot

# Librerías para cálculo numérico y generación de gráficas

import numpy as np
import control as ctrl
import matplotlib.pyplot as plt

# Datos de la simulación
x0,t0,tend,dt,w,h = 0,0,10,1E-3,7,3.5 #tiempo obtenido
N = round((tend-t0)/dt)+1
t = np.linspace(t0,tend,N)
u = np.where((t>=1)&(t<4),1.0,0.0) #Pulso de 1 V: sube en t=1 s y baja en t=4 s (como en Simulink)
 


#Funcion para entregar las funciones de transferencia segun el caso
def casos(Ra,Rv,Rp,Rf,Rb,Ls,Cs):
    # Carga de salida: Rf en paralelo con Rb
    Rs = (Rf*Rb)/(Rf+Rb)

    # Función de transferencia Vs(s)/Ve(s)
    num = [Cs*Rv*Rs,Rs]
    den = [Cs*Ls*(Ra+Rv),
           Ls + Cs*(Ra*(Rv+Rp+Rs) + Rv*(Rp+Rs)),
           Ra+Rp+Rs]
    sys = ctrl.tf(num, den)
    # Polos del sistema
    L= np.roots(den)
    return sys,L

#Funcion de transferencia del control
Ra,Rv,Rp,Rf,Rb,Ls,Cs = 1e3,1e3,1e3,100e3,10e3,100e-3,100e-6
sysControl,L = casos(Ra,Rv,Rp,Rf,Rb,Ls,Cs)
print(f"Funcion de transferencia del control:{sysControl}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2= {L[1]:.3e}\n")
#llamar funcion de transferencia del caso
Ra,Rv,Rp,Rf,Rb,Ls,Cs = 10e3,10e3,20e3,30e3,100e3,500e-3,100e-6
sysCaso,L = casos(Ra,Rv,Rp,Rf,Rb,Ls,Cs)
print(f"Funcion de transferencia del caso:{sysCaso}")
print(f"Polos del sistema: L1 = {L[0]:.3e}, L2= {L[1]:.3e}\n")


# Componentes del controlador I
kI = 1666.67668082261
Cr = 1e-6
Re = 1/(kI*Cr)
numI = [1]
denI = [Re*Cr,0]
CI = ctrl.tf(numI, denI)

# Sistema de control en lazo cerrado
print(f"Capacitancia Cr: {Cr} Faradios \n")
print(f"Resistencia Re: {Re} Ohms \n")
print(f"Funcion de transferencia del controlador I: {CI} \n")

#Colores
clr1 = np.array([80,3,192])/255
clr3 = np.array([171,3,169])/255
clr2 = np.array([255,213,30])/255
clr4 = np.array([157, 2, 235])/255

#Funciones del sistema en lazo abierto y lazo cerrado
_,Vsx = ctrl.forced_response(sysControl,t,u,x0) #Control
_,Vsy = ctrl.forced_response(sysCaso,t,u,x0) #Caso

sysI=ctrl.feedback(ctrl.series(CI,sysCaso),1,sign =-1) #I con caso
_,Vst = ctrl.forced_response(sysI,t,Vsx,x0) #I Tratamiento usando control

    
# Respuestas: Simulaciones numéricas
fg = plt.figure(1)
fg.set_size_inches(w,h)
plt.rcParams['font.size'] = 11
plt.rcParams['font.family'] = 'serif'
plt.rcParams['font.serif'] = ['Times New Roman']
plt.plot(t,u,'-',linewidth=1.0,color=clr4,label='Ve(t)')
plt.plot(t,Vsx,'--',linewidth=1.0,color=clr1,label='Vs(t) Control')
plt.plot(t,Vsy,'-',linewidth=1.0,color=clr2,label='Vs(t) Caso')
plt.plot(t,Vst,':',linewidth=1.5,color=clr3,label='PID(t) Tratamiento')
plt.xlim(0,10); plt.xticks(np.arange(0,11,1))
plt.ylim(-0.1,1.1); plt.yticks(np.arange(-0.1,1.1,0.1))
plt.xlabel('t [s]')
plt.ylabel('V(t) [V]')
plt.legend(bbox_to_anchor=(0.5,-0.25),loc='center',ncol=4,frameon=False)
plt.show()
fg.savefig('Tratamiento_python.pdf',bbox_inches='tight')
    