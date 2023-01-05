
import { CLT } from "./liquid-salary/liquid-salary.model";
import { PJSalary } from "./pj-salary/pj-salary.model";

export interface CompareOutputSchema {
    pj: PJSalary;
    clt: CLT;
}