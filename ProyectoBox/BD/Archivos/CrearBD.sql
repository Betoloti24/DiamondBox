-- ELIMINAR TABLAS
	drop table proyectobox.usuarios;
    drop table proyectobox.p_m;
    drop table proyectobox.productos;
    drop table proyectobox.materiales;
    drop table proyectobox.paises;
-- CREAR TABLAS
    -- TABLA DE USUARIOS
    create table proyectobox.usuarios (
        cod int primary key AUTO_INCREMENT,
        usuario nvarchar(20) UNIQUE,
        clave nvarchar(10) not null 
    );
    -- TABLA DE PRODUCTOS
    create table proyectobox.productos (
        cod int PRIMARY KEY auto_increment,
        nombre nvarchar(60) not null,
        precio float(10,2) not null,
        categoria nvarchar(15) not null,
        cantidad integer not null,
        imagen nvarchar(60) not null,

        constraint checkprecio_productos check (precio > 0),
        constraint checkcategoria_productos check (categoria in ('TIARA','ANILLO', 'COLLAR','PULSERA', 'ARETES'))
    );
    -- TABLA DE PAISES
    create table proyectobox.paises (
        cod int primary KEY auto_increment,
        abreviacion nvarchar(2) not null,
        nombre nvarchar(60) not null
    );
    -- TABLA DE PIEDRAS
    create table proyectobox.materiales (
        cod int primary key auto_increment,
        nombre nvarchar(20) not null,
        descripcion nvarchar(400) not null,
        precio float(10,2) not null,
        imagen nvarchar(20) not null,
        cantidad integer not null,
        corte nvarchar(20),
        origen int,

        constraint checkprecio_materiales check (precio > 0),
        constraint fk_pais FOREIGN KEY (origen) REFERENCES proyectobox.paises(cod)
    );
    ALTER TABLE proyectobox.materiales auto_increment = 19;
    -- TABLA DE PRODUCTOS Y SUS PIEDRAS
    create table proyectobox.p_m(
        cod_producto int not null,
        cod_material int not null,

        primary key (cod_producto,cod_material),
        constraint fk_producto FOREIGN KEY (cod_producto) REFERENCES proyectobox.productos(cod),
        constraint fk_materiales FOREIGN KEY (cod_material) REFERENCES proyectobox.materiales(cod)
    );