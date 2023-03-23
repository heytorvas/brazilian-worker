export interface CLTSalary {
    raw: number;
    earnings: number;
    medical_assistant: number;
    discounts: number;
    dependents: number;
    transport_voucher: any;
}

export interface CLTSalaryBase extends CLTSalary{
    inss: number,
    irrf: number,
    fgts: number,
    total: number
}

export interface CLT extends CLTSalaryBase {
    vacation: number;
    thirteenth: number;
}