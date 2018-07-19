import requests



class CandidatesAPI():
    def get_all_candidates(self):
        r = requests.get('http://qainterview.cogniance.com/candidates')
        return r

    def create_candidate(self,name,position):
        position = [position]
        name = [name]

        p = requests.post('http://qainterview.cogniance.com/candidates', json={'name':'vova','position':'super_qa'})
        return p







