import { Component, OnInit } from '@angular/core';
import { ClienteI } from 'src/app/components/models/cliente';
import { Router } from '@angular/router';
import { ClienteService } from '../../../services/cliente.service'

@Component({
  selector: 'app-mostrar-cliente',
  templateUrl: './mostrar-cliente.component.html',
  styleUrls: ['./mostrar-cliente.component.css']
})
export class MostrarClienteComponent implements OnInit {
  public clientes:any[] = []
  public displayedColumns: string[] = ["id", "nombreCliente", "direccionCliente", "telefonoCliente", "correoCliente","Acciones"]
  constructor(
    private clienteService: ClienteService,
    private router: Router
  ) { }

  ngOnInit(): void {
    this.mostrarClientes()
  }

  mostrarClientes() {
    this.clienteService.getAllCliente()
      .subscribe(
        data => this.clientes[0]=(data)
      )
  }
}
