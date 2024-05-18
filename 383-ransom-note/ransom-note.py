class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        counter={} 
        for c in magazine:
            if c in counter: 
                counter[c]+=1
            else:
                counter[c] = 1
    
        for c in ransomNote:
            if c not in counter: #primeiro check de valores
                return False
            elif counter[c] ==1: #check se foi a última ocorrência
                del counter[c]
            else:
                counter[c] -= 1 #retira o repetido
        return True
     