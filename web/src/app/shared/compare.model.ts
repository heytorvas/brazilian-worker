
import { CLT } from "../pages/liquid-salary/liquid-salary.model";
import { PJSalary } from "../pages/pj-salary/pj-salary.model";

export interface CompareOutputSchema {
    pj: PJSalary;
    clt: CLT;
}