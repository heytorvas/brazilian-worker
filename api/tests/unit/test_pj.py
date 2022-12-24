import pytest
from models.pj import PJBase
from services.pj import (
    _find_percentage_and_deduction,
    _get_tax_value,
    calculate_pj_salary,
    calculate_pj_salary_by_clt,
)


class TestPJModel:
    def test_valid_create_pj_salary_base(self):
        salary = PJBase(raw=5000, attachment='I')
        assert salary.raw == 5000
        assert salary.attachment == 'I'

        salary = PJBase(raw='5000', attachment='II')
        assert salary.raw == 5000
        assert salary.attachment == 'II'

    def test_invalid_create_pj_salary_base(self):
        with pytest.raises(ValueError):
            PJBase(raw='opa', attachment='I')

        with pytest.raises(ValueError):
            PJBase(attachment='opa')

        with pytest.raises(ValueError):
            PJBase(raw=5000, attachment='opa')


class TestPJService:
    @pytest.mark.parametrize(
        'attachment, percent',
        [('I', 4), ('II', 4.5), ('III', 6), ('IV', 4.5), ('V', 15.5)],
    )
    def test_get_percentage(self, attachment, percent):
        percentage, _ = _find_percentage_and_deduction(attachment, 7000)
        assert percentage == percent

    def test_get_tax_value(self):
        tax = _get_tax_value('I', 7000)
        assert tax == 280

    def test_calculate_pj_liquid_salary(self):
        input = PJBase(raw=7000, attachment='I')
        pj = calculate_pj_salary(input)

        assert pj.raw == 7000
        assert pj.attachment == 'I'
        assert pj.tax == 280
        assert pj.total == 6720

    def test_calculate_pj_salary_by_clt(self):
        input = PJBase(raw=7000, attachment='I')
        pj = calculate_pj_salary_by_clt(input)

        assert pj.raw == 7291.67
        assert pj.attachment == 'I'
        assert pj.tax == 291.67
        assert pj.total == 7000
