
import { CLT } from "../pages/clt-salary/clt-salary.model";
import { PJSalary } from "../pages/pj-salary/pj-salary.model";

export interface CompareOutputSchema {
    pj: PJSalary;
    clt: CLT;
}