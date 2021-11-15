from server import check_email, clubs


def test_check_right_email(monkeypatch):
	email = 'test@email.com'
	monkeypatch.setitem(clubs[0], 'email', email )
	assert check_email(email)


def test_check_wrong_email(monkeypatch):
	wrong_email = 'wrong_email@email.com'
	email = 'test@email.com'
	monkeypatch.setitem(clubs[0], 'email', email )
	assert check_email(wrong_email) == False