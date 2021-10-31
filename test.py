import pytest
import stack
import check

s = stack.Stack()

strings_positive = ('(((([{}]))))', '[([])((([[[]]])))]{()}', '{{[()]}}')
strings_negative = ('}{}', '{{[(])]}}', '[[{())}]')


class Test:

    def test_push(self):
        s.push('158')
        s.push('789')
        assert '158' in s.stack

    def test_pop(self):
        assert s.pop() == '789'

    def test_peek(self):
        s.push('690')
        assert s.peek() == '690'

    def test_size(self):
        assert s.size() == 2

    def test_isEmpty(self):
        assert s.isEmpty() is False

    @pytest.mark.parametrize('string', strings_positive)
    def test_check_positive(self, string):
        assert check.check_balance(string) is True

    @pytest.mark.parametrize('string', strings_negative)
    def test_check_negative(self, string):
        assert check.check_balance(string) is False
