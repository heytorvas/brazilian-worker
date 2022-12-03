export interface LiquidSalary {
    raw: number;
    earnings: number;
    medical_assistant: number;
    discounts: number;
}

export interface Salary extends LiquidSalary{
    inss: number,
    irrf: number,
    fgts: number,
    total: number
}