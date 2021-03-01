CREATE TABLE account
(
    id                integer primary key,
    password          varchar(128) not null,
    email             varchar(255) not null,
    username          varchar(255) not null,
    date_registration varchar(255) not null,
    last_login        varchar(255) not null,
    is_admin          integer      not null,
    is_staff          integer      not null,
    is_active         integer      not null,
    is_superuser      integer      not null,
    first_name        varchar(255) not null,
    last_name         varchar(255) not null,
    number            varchar(30)  not null
);

CREATE TABLE product
(
    id      integer primary key,
    title   varchar(255) not null,
    cart_id integer,
    FOREIGN KEY (cart_id) REFERENCES shop_cart (id)
);

CREATE TABLE shop_cart
(
    id                 integer primary key,
    total_products     integer not null,
    final_price        integer not null,
    in_order           integer not null,
    for_anonymous_user integer not null,
    owner_id           integer,
    FOREIGN KEY (owner_id) REFERENCES account (id)
);

CREATE TABLE shop_order
(
    id          integer primary key,
    first_name  varchar(255)  not null,
    last_name   varchar(255)  not null,
    phone       varchar(255)  not null,
    status      varchar(255)  not null,
    buying_type varchar(255)  not null,
    comment     varchar(255),
    created_at  varchar(255)  not null,
    order_date  varchar(255)  not null,
    address     varchar(1024) not null,

    cart_id     integer       not null,
    customer_id integer       not null,

    FOREIGN KEY (cart_id) REFERENCES shop_cart (id),
    FOREIGN KEY (customer_id) REFERENCES account (id)

);
