import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'Portal do Trabalhador';

  dependents = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

  numberOnly(event): boolean {
    const charCode = (event.which) ? event.which : event.keyCode;
    if (charCode > 31 && (charCode < 48 || charCode > 57)) {
        return false;
    }
    return true;
  }

  removeUndefined(obj: Object) {
    Object.keys(obj).forEach(key => obj[key] === undefined && delete obj[key]);
    return obj
  }
}
