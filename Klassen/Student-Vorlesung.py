class Student:
    def __init__ (self, vn, nn):
        self.vorname = vn
        self.nachname = nn
 
class Vorlesung:
    def __init__ (self, n):
         self.bezeichnung = n
         self.studenten=[]

    def addstudent (self, st):
         self.studenten.append(st)
         print ("*** Studi eingefügt ***")
         
    def ausgabestudis(self):
        print ("\nVorlesung:", self.bezeichnung)
        print ("Studenten:")
        for studi in self.studenten:
            print (studi.vorname, studi.nachname)
 
v = Vorlesung ("Python for Beginners")
s1 = Student ("Harry", "Hirsch")
s2 = Student ("Erna", "Nickelmeier")

v.addstudent (s1)
v.addstudent (s2)
v.ausgabestudis ()
