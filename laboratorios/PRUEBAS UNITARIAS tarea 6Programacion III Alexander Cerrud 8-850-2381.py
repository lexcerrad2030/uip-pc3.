'''
tarea # 6 de programacion 3 Alexander Cerrud 8-850-2381
 '''

import unittest

class registro:
    try:
        def registro(self,usuario,edad):
            usuario=input("escribe tu nombre")
            edad=input("escribe tu edad")
            return {"usuario:":usuario,"apellido":usuario+"Baso","edad:":edad}
    except Exception:
        print("ERROR")

class NotificationsTestCase(unittest.TestCase):
    try:

        def test_user_repository(self):
            users=registro()
            user=users.registro("lex","18")

            self.assertEquals("lexbaso",user['apellido'])
    except Exception:
        print("ERROR")

if __name__ == '__main__':
        unittest.main()
