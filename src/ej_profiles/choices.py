from django.utils.translation import ugettext_lazy as _

from boogie import IntEnum


class Race(IntEnum):
    UNDECLARED = 0, _('Undeclared')
    BLACK = 1, _('Black')
    BROWN = 2, _('Brown')
    WHITE = 3, _('White')
    YELLOW = 4, _('Yellow')
    INDIGENOUS = 5, _('Indigenous')
    DO_NOT_KNOW = 6, _('Do not know')


class Gender(IntEnum):
    UNDECLARED = 0, _('Undeclared')
    FEMALE = 1, _('Female')
    MALE = 2, _('Male')
    CIS_FEMALE = 3, _('Cis Female')
    CIS_MALE = 4, _('Cis Male')
    AGENDER = 5, _('Agender')
    GENDERQUEER = 6, _('Genderqueer')
    GENDERFLUID = 7, _('Genderfluid')
    NON_CONFORMIST_GENDER = 8, _('Non conformist gender')
    VARIANT_GENDER = 9, _('Variant gender')
    INTERSEX = 10, _('Intersex')
    NON_BINARY = 11, _('Non binary')
    TRANSGENDERED = 12, _('Transgendered')
    PANGENDER = 13, _('Pangender')
    TRANSSEXUAL_WOMAN = 14, _('Transsexual woman')
    TRANSSEXUAL_MAN = 15, _('Transsexual man')
    TRANSFEMINAL = 16, _('Transfeminal')
    TRANSMASCULINE = 17, _('Transmasculine')
    DO_NOT_KNOW = 18, _('Do not know')
    NONE = 19, _('None')
    OTHER = 20, _('Other')
