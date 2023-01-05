export interface LiquidSalary {
    raw: number;
    earnings: number;
    medical_assistant: number;
    discounts: number;
    dependents: number;
    transport_voucher: any;
}

export interface Salary extends LiquidSalary{
    inss: number,
    irrf: number,
    fgts: number,
    total: number
}

export interface CLT extends Salary {
    vacation: number;
    vacation_one_third: number;
    thirteenth: number;
}