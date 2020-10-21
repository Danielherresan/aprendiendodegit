import persona as p
import estudiante as es 
import egresado as eg
laura = p.Persona('Laura',18,28137231)
mario =p.Persona('Mario', 20, 21442214)
valeria = es.Estudiante('Valeria',18,215346,'Biomédica',3)
laura.hablar('Todo anda muy bien, me gusta aprender')
mario.comer('Taco')
valeria.estudiar('cálculo')
melany = eg.Egresado('Melany',18,143413,'Biomédica','2023/12/12')
print (melany.semestre)
melany.trabajar('MIT')
