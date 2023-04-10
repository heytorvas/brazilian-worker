import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CLTSalaryComponent } from './pages/clt-salary/clt-salary.component';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CurrencyMaskConfig, CurrencyMaskModule, CURRENCY_MASK_CONFIG } from "ng2-currency-mask";
import { HomeComponent } from './components/home/home.component';
import { FooterComponent } from './components/footer/footer.component';
import { PageNotFoundComponent } from './pages/page-not-found/page-not-found.component';
import { HeaderComponent } from './components/header/header.component';
import { PjSalaryComponent } from './pages/pj-salary/pj-salary.component';
import { LoadingComponent } from './shared/loading/loading.component';
import { PjCltComponent } from './pages/pj-clt/pj-clt.component';
import { CltPjComponent } from './pages/clt-pj/clt-pj.component';
import { ThirteenthComponent } from './pages/thirteenth/thirteenth.component';
import { AlertModalComponent } from './shared/alert-modal/alert-modal.component';
import { HourComponent } from './pages/hour/hour.component';
import { DigitOnlyModule } from '@uiowa/digit-only';

export const WebCurrencyMaskConfig: CurrencyMaskConfig = {
  prefix: 'R$',
  allowNegative: false,
  thousands: '.',
  decimal: ',',
  align: 'left',
  precision: 2,
  suffix: '',
};

@NgModule({
  declarations: [
    AppComponent,
    CLTSalaryComponent,
    HomeComponent,
    FooterComponent,
    PageNotFoundComponent,
    HeaderComponent,
    PjSalaryComponent,
    LoadingComponent,
    PjCltComponent,
    CltPjComponent,
    ThirteenthComponent,
    AlertModalComponent,
    HourComponent
    
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    CurrencyMaskModule,
    DigitOnlyModule
  ],
  bootstrap: [AppComponent],
  providers: [
    { provide: CURRENCY_MASK_CONFIG, useValue: WebCurrencyMaskConfig }
  ]
})
export class AppModule { }
