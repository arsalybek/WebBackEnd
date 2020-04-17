import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CommonModule } from '@angular/common';
import {CompanyListComponent} from './company-list/company-list.component';
import {CompanyVacancyListComponent} from './company-vacancy-list/company-vacancy-list.component';

const routes: Routes = [
  {path: '', component: CompanyListComponent},
  {path: 'companies/:id/vacancies', component: CompanyVacancyListComponent},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
