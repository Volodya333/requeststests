import candidates_api
import json

def test_get_all_candidates():
    api = candidates_api.CandidatesAPI()
    response = api.get_all_candidates()
    assert response.status_code == 200

def create_candidate():
    api = candidates_api.CandidatesAPI()
    response = api.create_candidate('vova','super_qa')
    assert response.status_code == 201
    json_response = json.loads(response.content)

    assert json_response['candidate']['id'] > 0
    assert json_response['candidate']['name'] == "vova"
    assert json_response['candidate']['position'] == "super_qa"














test_get_all_candidates()
create_candidate()









