import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateProcuctComponent } from './create-procuct.component';

describe('CreateProcuctComponent', () => {
  let component: CreateProcuctComponent;
  let fixture: ComponentFixture<CreateProcuctComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ CreateProcuctComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(CreateProcuctComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
