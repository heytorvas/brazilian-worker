export interface PJSalaryBase {
    raw: number;
    attachment: string;
}

export interface PJSalary extends PJSalaryBase {
    tax: number;
    total: number;
}