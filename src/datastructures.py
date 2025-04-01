
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._next_id = 1
        self._members = []

    # Este método genera un 'id' único al agregar miembros a la lista (no debes modificar esta función)
    def _generate_id(self):
        generated_id = self._next_id
        self._next_id += 1
        return generated_id

    ## Debes implementar este método
    ## Agrega un nuevo miembro a la lista de _members
    def add_member(self, member):
        member["id"] = self._generate_id()
        member["last_name"] = self.last_name
        member["lucky_numbers"] = list(member.get("lucky_numbers", set()))
        self._members.append(member)
        return(member)
        
        ## Debes implementar este método
        ## Recorre la lista y elimina el miembro con el id proporcionado

    def delete_member(self, id):
        for position in range(len(self._members)):
            if self._members[position]["id"] == id:
                self._members.pop(position)
                
                return None
            
    ## Debes implementar este método
    ## Recorre la lista y obtén el miembro con el id proporcionado  

    def get_member(self, id):
        for position in self._members:
            if position["id"] == int(id):
                return position

    def get_all_members(self, id):
        return self._members
