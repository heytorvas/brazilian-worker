import pytest
from domain.models.clt import CLTBase
from resources.services.clt import (
    INSS_DATA,
    IRRF_DATA,
    _calculate_fgts_value,
    _calculate_inss_value,
    _calculate_irrf_value,
    _calculate_transport_voucher,
    _find_percentage_and_deduction,
    calculate_clt_salary_by_pj,
    calculate_liquid_value,
)


class TestCLTModel:
    def test_valid_create_salary_base(self):
        salary = CLTBase(raw=2300)
        assert salary.raw == 2300
        assert salary.earnings == 0

        salary = CLTBase(raw="2300")
        assert salary.raw == 2300
        assert salary.earnings == 0

    def test_invalid_create_salary_base(self):
        with pytest.raises(ValueError):
            CLTBase(raw="opa")


class TestCLTService:
    def test_get_percentage_and_deduction_from_inss(self):
        percentage, deduction = _find_percentage_and_deduction(INSS_DATA, 2000)

        assert float(percentage) == 9
        assert deduction == 18.18

    @pytest.mark.parametrize("raw,percent,ded", [(2000, 0, 0), (2500, 7.5, 158.4)])
    def test_get_percentage_and_deduction_from_irrf(self, raw, percent, ded):
        percentage, deduction = _find_percentage_and_deduction(IRRF_DATA, raw)

        assert float(percentage) == percent
        assert deduction == ded

    def test_calculate_liquid_salary(self):
        input = CLTBase(raw=3000)
        salary = calculate_liquid_value(input)

        assert salary.raw == 3000
        assert salary.discounts == 0
        assert salary.earnings == 0
        assert salary.dependents == 0
        assert salary.transport_voucher == 0
        assert salary.medical_assistant == 0
        assert salary.fgts == 240
        assert salary.inss == 269
        assert salary.irrf == 46.42
        assert salary.total == 2684.58

    def test_calculate_transport_voucher(self):
        salary = 2000
        voucher = 120

        assert _calculate_transport_voucher(salary, "true") == voucher
        assert _calculate_transport_voucher(salary, "True") == voucher
        assert _calculate_transport_voucher(salary, "TRUE") == voucher
        assert _calculate_transport_voucher(salary, True) == voucher
        assert _calculate_transport_voucher(salary, "false") == 0
        assert _calculate_transport_voucher(salary, "False") == 0
        assert _calculate_transport_voucher(salary, "FALSE") == 0
        assert _calculate_transport_voucher(salary, False) == 0

    @pytest.mark.parametrize(
        "salary,inss,value",
        [(3000, 269, 46.42), (4000, 396.18, 170.17), (5000, 536.18, 352.63)],
    )
    def test_calculate_irrf_without_dependents(self, salary, inss, value):
        assert _calculate_irrf_value(salary, inss, dependents=0) == value

    @pytest.mark.parametrize("dependent,value", [(1, 32.21), (2, 17.99), (3, 3.77)])
    def test_calculate_irrf_with_dependents(self, dependent, value):
        assert (
            _calculate_irrf_value(salary=3000, inss=269, dependents=dependent) == value
        )

    @pytest.mark.parametrize("fgts,value", [(3000, 240), (4000, 320)])
    def test_calculate_fgts(self, fgts, value):
        assert _calculate_fgts_value(fgts) == value

    @pytest.mark.parametrize(
        "salary,value", [(3000, 269), (4000, 396.18), (5000, 536.18)]
    )
    def test_calculate_inss(self, salary, value):
        assert _calculate_inss_value(salary) == value

    def test_calculate_clt_salary_by_pj(self):
        input = CLTBase(raw=7000)
        clt = calculate_clt_salary_by_pj(input)

        assert clt.total == 6999.95
        assert clt.raw == 7044.0
        assert clt.inss == 822.34
        assert clt.irrf == 826.00
        assert clt.fgts == 563.52
        assert clt.vacation == 591.13
        assert clt.thirteenth == 449.64
