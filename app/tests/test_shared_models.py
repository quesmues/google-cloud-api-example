from app.api.v1.shared_models import Marca, Modelo


def test_model_marca(marca_fixture):
    resumo = Marca(**marca_fixture)

    assert resumo.nome

def test_model_modelo(modelo_fixture):
    resumo = Modelo(**modelo_fixture)

    assert resumo.nome