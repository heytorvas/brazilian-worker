import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { LiquidSalary } from './liquid-salary.model';

@Component({
    selector: 'app-liquid-salary',
    templateUrl: './liquid-salary.component.html',
    styleUrls: ['./liquid-salary.component.css']
})

export class LiquidSalaryComponent implements OnInit {
    formLiquidSalary!: FormGroup;

    constructor(private formBuilder: FormBuilder) { }

    ngOnInit() {
        this.createForm(new LiquidSalary());
    }

    createForm(salary: LiquidSalary) {
        this.formLiquidSalary = this.formBuilder.group({
            raw: [salary.raw],
            earnings: [salary.earnings],
            medical_assistant: [salary.medical_assistant],
            discounts: [salary.discounts]
        })
    }

    onSubmit(){
        console.log(this.formLiquidSalary.value);
    }
}