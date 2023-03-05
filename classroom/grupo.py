from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"

    def __init__(self, grupo = "grupo predeterminado", asignaturas = None, estudiantes= None):
        self._grupo = grupo
        if asignaturas is None:
            _asignaturas = []
        else:
            _asignaturas = asignaturas
        self._asignaturas = _asignaturas
        if estudiantes is None:
            _listadoAlumnos = []
        else:
            _listadoAlumnos = estudiantes
        self.listadoAlumnos = _listadoAlumnos

    def listadoAsignaturas(self, **kwargs):
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno, lista=None):
        if lista is None:
            _lista = []
        else:
            _lista = lista
        _lista.append(alumno)
        self.listadoAlumnos = self.listadoAlumnos + _lista

    def __str__(self):
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre