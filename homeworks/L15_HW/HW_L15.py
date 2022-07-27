
#  1 завдання: реалізувати методи як описано в докстрінгах до кожного з них
#  2 завдання: написати тести на кожну з функцій, написати тести для особливих випадків, наприклад
#  відправити повідомлення для неіснуючого юзера (повинні отримати UserNotFound)
#  скасувати повідомлення, а потім намагатись його отримати (повинні отримати MessageNotFound)

import uuid
from unittest import TestCase

import datetime as dt


class UserNotFound(Exception):
    pass


class MessageNotFound(Exception):
    pass


class User:
    def __init__(self, name):
        self.id = uuid.uuid4()
        self.name = name
        self.incoming_messages = []
        self.outgoing_messages = []

    def add_message(self, message_obj, is_incoming=True):
        """
        Додає повідомлення в incoming_messages чи outgoing_messages в залежності від is_incoming
        :param message_obj:
        :param is_incoming:
        :return:
        """
        if is_incoming:
            self.incoming_messages[message_obj] = message_obj.id
        elif not is_incoming:
            self.outgoing_messages[message_obj] = message_obj.id
        return 'message added'

    @property
    def get_last_message(self):
        """
        Повертає останнє вхідне повідомлення
        :return:
        """
        return self.incoming_messages[-1]

    def get_all_messages(self, include_incoming=True, include_outgoing=True):
        """
        Повертає словник виду
        {
            "incomings": list of messages, - за умови що include_incoming True, інакше None
            "outgoings": list of messages, - за умови що include_outgoing True, інакше None
        }
        :param include_incoming:
        :param include_outgoing:
        :return:
        """
        return {"incomings": self.incoming_messages if include_incoming else None,
                "outgoings": self.outgoing_messages if include_outgoing else None}

    def read_last_message(self):
        """
        повертає останнє повідомлення, саме повідомлення видаляється з incoming_messages
        :return:
        """
        return self.incoming_messages.pop()

    def read_all_messages(self):
        """
        повертає список всіх вхідних повідомлень, і очищає даний список
        :return:
        """
        a_i_m = self.incoming_messages.copy()
        self.incoming_messages.clear()
        return a_i_m

    def get_message_by_id(self, id):
        pass


def get_message_by_id(self, message_id, include_incoming=True, include_outgoing=True):
    """
        знайти повідомлення по його ід, include_incoming, include_outgoing визначають в якому контейнері шукати
        якщо повідомлення немає, згенерувати ексепшин MessageNotFound
        :param self:
        :param message_id:
        :param include_incoming:
        :param include_outgoing:
        :return:
        """
    if include_incoming:
        for key, value in self.incoming_messages.items():
            if message_id == value:
                return key
    if include_outgoing:
        for key, value in self.outgoing_messages.items():
            if message_id == value:
                return key
    raise MessageNotFound


class Message:
    def __init__(self, user_from, user_to, date, text):
        self.id = uuid.uuid4()
        self.user_from = user_from
        self.user_to = user_to
        self.date = date
        self.text = text

    def edit(self, new_text):
        """
        змінює текст повідомлення
        :return:
        """
        self.text = new_text
        return self


class MessageHelper:
    @classmethod
    def send_message(cls, user_from_id, user_to_id, param):
        pass


def send_message(user_from_id, user_to_id, text, user_from, user_to, date):
    """
    створює обєкт повідомлення
    записує цей обєкт в вхідні повідомлення для user_to, і в вихідні для user_from
    Важливо! перевірити чи юзери існують в базі даних
    :param date:
    :param user_to:
    :param user_from:
    :type text: object
    :param user_from_id:
    :param user_to_id:
    :param text:
    :return:
    """
    if user_from_id not in UserHelper.users_db or user_to_id not in UserHelper.users_db:
        raise UserNotFound
    else:
        UserHelper.get_user(user_from_id)
        UserHelper.get_user(user_to_id)
        new_message = Message(user_from, user_to, date, text)
        user_to.add_message(new_message)
        user_from.add_message(new_message, is_incoming=False)
    return new_message


def unsend_message(message):
    """
        Видаляє повідомлення у двох юзерів
        :return:
        """
    message.user_to.incoming_messages.remove(message)
    message.user_from.outgoing_messages.remove(message)


class UserHelper:
    users_db = {

    }

    @classmethod
    def create_user(cls, name):
        """
        створює юзера записує його в users_db, повертає ід юзера
        приклад
            user_db[user.id] = user
        :param name:
        :return:
        """
        new_user = User(name)
        cls.users_db[new_user.id] = new_user
        return new_user.id

    @classmethod
    def get_user(cls, user_to_id):
        pass


def get_user(cls, id):
    """
        Повертає юзера, якщо юзера немає, генерує ексепшн
        :param cls:
        :param id:
        :return:
        """
    try:
        user_it = cls.users_db[id]
        return user_it
    except KeyError:
        raise UserNotFound


def delete_user(cls, id):
    """
    Видаляє юзера з users_db
    :param cls:
    :param id:
    :return:
    """
    try:
        del cls.users_db[id]
        return True
    except KeyError:
        raise UserNotFound


class TestUser(TestCase):
    def setUp(self):
        self.user_from = User("user_from")
        self.user_to = User("user_to")
        self.message = Message(self.user_from, self.user_to, dt.datetime.now(), 'test message')
        self.message1 = Message(self.user_to, self.user_from, dt.datetime.now(), 'test message1')
        self.message2 = Message(self.user_from, self.user_to, dt.datetime.now(), 'test message2')
        for message in [self.message, self.message1, self.message2]:
            self.user_to.add_message(message)

    def tearDown(self):
        del (self.user_from, self.user_to, self.message)

    def test_add_message(self):
        self.user_to.add_message(self.message)
        self.assertIn(self.message, self.user_to.incoming_messages)

    def test_get_last_message(self):
        self.assertEqual(self.user_to.incoming_messages[-1], self.message2)

    def test_get_all_messages(self):
        self.assertEqual(self.user_to.get_all_messages(True, True), {"incomings": [self.message, self.message2],
                                                                     "outgoings": [self.message1]})
        self.assertEqual(self.user_to.get_all_messages(False, True), {"incomings": None,
                                                                      "outgoings": [self.message1]})

    def test_read_last_message(self):
        self.assertEqual(self.user_to.read_last_message(), self.message2)
        self.assertEqual(self.user_to.incoming_messages[-1], self.message)

    def test_read_all(self):
        self.assertEqual(self.user_to.read_all_messages(), [self.message, self.message2])
        self.assertEqual(self.user_to.incoming_messages, [])

    def test_get_message_by_id(self):
        self.assertEqual(self.user_to.get_message_by_id(self.message.id), self.message)


class TestMessage(TestCase):
    def setUp(self):
        self.user_from = User("UserFrom")
        self.user_to = User("UserTo")
        self.message = Message(self.user_from, self.user_to, dt.datetime.now(), 'test message')

    def tearDown(self):
        del (self.user_from, self.user_to, self.message)

    def test_edit(self):
        self.message.edit("new text")
        self.assertEqual(self.message.text, "new text")


class TestMessageHelper(TestCase):
    def setUp(self):
        self.user_from_id = UserHelper.create_user("UserFrom")
        self.user_to_id = UserHelper.create_user("UserTo")
        MessageHelper.send_message(self.user_from_id, self.user_to_id, "This lecture is difficult!")
        self.message = self.user_to.get_last_message()

    def tearDown(self):
        del (self.user_from_id, self.user_to_id)

    def test_send_message(self):
        self.assertEqual(UserHelper.get_user(self.user_to_id).get_last_message().text,
                         "This lecture is difficult!")
        self.assertEqual(UserHelper.get_user(self.user_from_id).outgoing_messages[-1].text,
                         "HThis lecture is difficult!")
        us = User("Fail")
        with self.assertRaises(UserNotFound):
            MessageHelper.send_message(self.user_from_id, us.id, "???")

    def test_unsend_message(self):
        message_id = self.messege.id
        MessageHelper.unsend_message(self.message)
        with self.assertRaises(MessageNotFound):
            self.user_to.get_message_by_id(message_id)


class TestUserHelper(TestCase):
    def setUp(self):
        self.user_helper = UserHelper
        self.user_id = self.user_helper.create_user("Cat")

    def tearDown(self):
        del self.user_helper

    def test_create_user(self):
        self.assertIn(self.user_id, self.user_helper.users_db)

    def test_get_user(self):
        self.assertEqual(self.user_helper.get_user(self.user_id), "Cat")

    def test_delete_user(self):
        self.user_helper.delete_user(self.user_id)
        with self.assertRaises(UserNotFound):
            self.user_helper.get_user(self.user_id)
