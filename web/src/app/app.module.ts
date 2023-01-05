import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LiquidSalaryComponent } from './liquid-salary/liquid-salary.component';

import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { CurrencyMaskModule } from "ng2-currency-mask";
import { LiquidSalaryService } from './liquid-salary/liquid-salary.service';
import { HomeComponent } from './home/home.component';
import { FooterComponent } from './footer/footer.component';
import { PageNotFoundComponent } from './page-not-found/page-not-found.component';
import { HeaderComponent } from './header/header.component';
import { PjSalaryComponent } from './pj-salary/pj-salary.component';
import { LoadingComponent } from './loading/loading.component';

@NgModule({
  declarations: [
    AppComponent,
    LiquidSalaryComponent,
    HomeComponent,
    FooterComponent,
    PageNotFoundComponent,
    HeaderComponent,
    PjSalaryComponent,
    LoadingComponent
    
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    CurrencyMaskModule
  ],
  providers: [LiquidSalaryService],
  bootstrap: [AppComponent]
})
export class AppModule { }
