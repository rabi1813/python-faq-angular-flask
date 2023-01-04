import { Component } from '@angular/core';
import { CommonServiceService } from './services/common-service.service';
import { CommonModels } from './models/common-models.model';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'python-faq-angular-flask';
  todoArray : string[]=[];
  configData: any;
  displayedColumns: string[] = ["system_id", "name" ,"test_boolean", "test_date", "test_date2", "test_null"]

  constructor(private configService: CommonServiceService) {
    this.showConfig()
  }

  addTodo(value: string){
    this.todoArray.push(value)
    console.log(this.todoArray)
  }

  showConfig() {
    this.configService.getDataType()
      .subscribe((data => {
        console.log(data)
        this.configData = data;
      }));
  }
}
