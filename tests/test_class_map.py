from wtforms_alchemy.utils import ClassMap


class A(object):
    pass


class B(object):
    pass


class A2(A):
    pass


class B2(B):
    pass


class C(object):
    pass


def test_contains_with_subclass_check():
    class_map = ClassMap({A: 3, B: 6})
    assert B2 in class_map
    assert B in class_map
    assert A in class_map
    assert A2 in class_map


def test_contains_with_isinstance_check():
    class_map = ClassMap({A: 3, B: 6})
    assert B2() in class_map
    assert B() in class_map
    assert A() in class_map
    assert A2() in class_map
