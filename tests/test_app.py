from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá mundo!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Paulo',
            'email': 'paulo@mail.com',
            'password': 'password',
        },
    )  # Act

    assert response.status_code == HTTPStatus.CREATED  # Assert
    assert response.json() == {
        'id': 1,
        'username': 'Paulo',
        'email': 'paulo@mail.com',
    }  # Assert


def test_read_users(client):
    response = client.get('/users/')  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'Paulo',
                'email': 'paulo@mail.com',
            }
        ]
    }  # Assert


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'Paulinho',
            'email': 'paulinho@mail.com',
            'password': 'password',
            'id': 1,
        },
    )  # Act

    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {
        'id': 1,
        'username': 'Paulinho',
        'email': 'paulinho@mail.com',
    }  # Assert


def test_delete_user(client):
    response = client.delete('/users/1')  # Act

    # assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'User deleted'}  # Assert
