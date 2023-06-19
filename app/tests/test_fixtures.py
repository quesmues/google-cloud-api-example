import uuid

import pytest


@pytest.fixture
def marca_fixture() -> dict:
    return {"codigo": "teste", "nome": "teste"}


@pytest.fixture
def modelo_fixture() -> dict:
    return {"codigo": "teste", "nome": "teste"}

@pytest.fixture
def veiculo_fipe_fixture(modelo_fixture) -> dict:
    return {"codigo": uuid.uuid4(), "modelo": modelo_fixture, "observacoes": None}


@pytest.fixture
def marcaform_fixture() -> dict:
    return {"marca": marca_fixture}

@pytest.fixture
def veiculo_tasks_fixture(marca_fixture, modelo_fixture) -> dict:
    return {"codigo": uuid.uuid4(), "marca": marca_fixture, "modelo": modelo_fixture, "observacoes": None}

@pytest.fixture
def message_fixture() -> dict:
    return {"detail": "teste"}