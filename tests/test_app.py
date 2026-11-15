from fastapi.testclient import TestClient
from http import HTTPStatus

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A : Arrange - Arranjo
    - A : Act     - Ação/Agir/ Chama o bloco de codigo / Executa a coisa (o SUT)
    - A : Assert  - Garanta que A é A
    """

    # arrange
    client = TestClient(app)

    # Act
    response = client.get('/')
#
    # Assert
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


