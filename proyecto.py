from abc import ABCMeta, abstractmethod
from itertools import cycle

class Asignatura:
    def __init__(self, codigo, descripcion, planEstudios) :
        self.codigo = codigo
        self.descripcion = descripcion
        self.planEstudios = planEstudios
        self.estudiantes = []
    def addEstudiantes(self, rut):
        self.estudiantes.append(rut)
    def delEstudiantes(self, rut):
        self.estudiantes.remove(rut)
    def getEstudiantes(self):
        return self.estudiantes

class Actividad:
    def __init__(self, codigo, descripcion) :
        self.codigo = codigo
        self.descripcion = descripcion
        self.estudiantes = []
    def addEstudiantes(self, rut):
        self.estudiantes.append(rut)
    def delEstudiantes(self, rut):
        self.estudiantes.remove(rut)
    def getEstudiantes(self):
        return self.estudiantes

class PersonaA(metaclass=ABCMeta):
    @abstractmethod
    def rutEsValido(self):
        pass

class Validar():
    def esRut(rut):
        pass

    def esRut(rut):
        rut = rut.upper();
        rut = rut.replace("-","")
        rut = rut.replace(".","")
        aux = rut[:-1]
        dv = rut[-1:]
    
        revertido = map(int, reversed(str(aux)))
        factors = cycle(range(2,8))
        s = sum(d * f for d, f in zip(revertido,factors))
        res = (-s)%11
    
        if str(res) == dv:
            return True
        elif dv=="K" and res==10:
            return True
        else:
            return False

class Persona(PersonaA, Validar):

    def __init__(self, rut, nombre, apellido, direccion):
        self.rut = rut
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion    

    def rutEsValido(self):
        return Validar.esRut(self.rut)

class Estudiante(Persona):
    def __init__(self, *arg):
        if len(arg) == 5:
            self.anio = arg[-1]
        super().__init__(*arg[0:-1])

class Apoderado(Persona):
    def __init__(self, rut, nombre, apellido, direccion):
        self.estudiantes = []
        super().__init__(rut, nombre, apellido, direccion)
    def addEstudiantes(self, rut):
        self.estudiantes.append(rut)
    def delEstudiantes(self, rut):
        self.estudiantes.remove(rut)
    def getEstudiantes(self):
        return self.estudiantes
        

estudiante1 = Estudiante("13834450-1","Andres","Santillana","Santa Isabel 10852",2019)
estudiante2 = Estudiante("13834570-k","Jorge","Peñaloza","Maria Elena 334",2020)
estudiante3 = Estudiante("20552211-1","Valentina","Peñaloza","Las Magnolias 1122",2021)

apoderado1 = Apoderado("6225225-8","Segundo","Peñaloza","Los Copihues 2234")
apoderado1.addEstudiantes(estudiante1.rut)
apoderado1.addEstudiantes(estudiante2.rut)
apoderado1.addEstudiantes(estudiante3.rut)
apoderado2 = Apoderado("8258963-1","Ruben","Santillana","Los Magnus 34")
apoderado2.addEstudiantes(estudiante1.rut)

print(apoderado1.rut, apoderado1.nombre, apoderado1.apellido, apoderado1.direccion, apoderado1.rutEsValido())
print("Hay un estudiante que no corresponde")
for rutEstudiante in apoderado1.getEstudiantes():
    print(apoderado1.nombre, "es apoderado de", rutEstudiante)

apoderado1.delEstudiantes(estudiante1.rut)

print("Ahora si estan los 2 estudiantes que corresponden")
for rutEstudiante in apoderado1.getEstudiantes():
    print(apoderado1.nombre, "es apoderado de", rutEstudiante)


print("El otro apoderado es")
print(apoderado2.rut, apoderado2.nombre, apoderado2.apellido, apoderado2.direccion, apoderado2.rutEsValido())
for rutEstudiante in apoderado2.getEstudiantes():
    print(apoderado2.nombre, "es apoderado de", rutEstudiante)

print("Los estudiantes son")
print(estudiante1.rut, estudiante1.nombre, estudiante1.apellido, estudiante1.direccion, estudiante1.anio, estudiante1.rutEsValido())
print(estudiante2.rut, estudiante2.nombre, estudiante2.apellido, estudiante2.direccion, estudiante2.anio, estudiante2.rutEsValido())
print(estudiante3.rut, estudiante3.nombre, estudiante3.apellido, estudiante3.direccion, estudiante3.anio, estudiante3.rutEsValido())

clon = estudiante1
print("el clon es")
clon.nombre = "Andrea"
print(estudiante1.rut, estudiante1.nombre, estudiante1.apellido, estudiante1.direccion, estudiante1.anio, estudiante1.rutEsValido())

ingles = Asignatura(101,"Ingles Basico", "Verbos")
ingles.addEstudiantes(estudiante1.rut)
print("Asignatura",ingles.codigo, ingles.descripcion, "Alumno",ingles.getEstudiantes()[0])

natacion = Actividad(522,"Natacion en estadio municipal")
natacion.addEstudiantes(estudiante2.rut)
natacion.addEstudiantes(estudiante3.rut)

print("Asignatura",natacion.codigo, natacion.descripcion, "Alumno",natacion.getEstudiantes()[0])
print("Asignatura",natacion.codigo, natacion.descripcion, "Alumno",natacion.getEstudiantes()[1])