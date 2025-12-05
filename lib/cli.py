import click
from functions import (
    create_apartment, list_apartments, find_apartment, delete_apartment, get_apartment_tenants, update_apartment,
    create_tenant, list_tenants, find_tenant, delete_tenant, get_tenant_payments, update_tenant,
    create_payment, list_payments, find_payment, delete_payment, update_payment
)

# ----------------------------------------------------
# MAIN CLICK GROUP
# ----------------------------------------------------
@click.group()
def cli():
    """Apartment Management CLI"""
    pass


# ----------------------------------------------------
# APARTMENT COMMANDS
# ----------------------------------------------------
@cli.group()
def apartment():
    """Apartment related commands"""
    pass

@apartment.command()
@click.option("--number", prompt="Apartment number")
@click.option("--unit_type", prompt="Unit type")
@click.option("--rent", prompt="Rent amount", type=int)
def create(number, unit_type, rent):
    apt = create_apartment(number, unit_type, rent)
    click.echo(f"Apartment created: {apt}")

@apartment.command()
def list():
    apartments = list_apartments()
    for a in apartments:
        click.echo(a)

@apartment.command()
@click.argument("id", type=int)
def find(id):
    apt = find_apartment(id)
    click.echo(apt or "Apartment not found")

@apartment.command()
@click.argument("id", type=int)
def delete(id):
    if delete_apartment(id):
        click.echo("Apartment deleted")
    else:
        click.echo("Apartment not found")

@apartment.command()
@click.argument("id", type=int)
def tenants(id):
    t = get_apartment_tenants(id)
    if t:
        for tenant in t:
            click.echo(tenant)
    else:
        click.echo("No tenants or apartment not found")

@apartment.command()
@click.argument("id", type=int)
@click.option("--number", default=None)
@click.option("--unit_type", default=None)
@click.option("--rent_amount", type=int, default=None)
def update(id, number, unit_type, rent_amount):
    apt = update_apartment(id, number, unit_type, rent_amount)
    if apt:
        click.echo(f"Apartment updated: {apt}")
    else:
        click.echo("Apartment not found")



# ----------------------------------------------------
# TENANT COMMANDS
# ----------------------------------------------------
@cli.group()
def tenant():
    """Tenant related commands"""
    pass

@tenant.command()
@click.option("--name", prompt="Tenant name")
@click.option("--phone", prompt="Phone number")
@click.option("--apartment_id", prompt="Apartment ID", type=int)
def create(name, phone, apartment_id):
    t = create_tenant(name, phone, apartment_id)
    click.echo(f"Tenant created: {t}")

@tenant.command()
def list():
    tenants = list_tenants()
    for t in tenants:
        click.echo(t)

@tenant.command()
@click.argument("id", type=int)
def find(id):
    t = find_tenant(id)
    click.echo(t or "Tenant not found")

@tenant.command()
@click.argument("id", type=int)
def delete(id):
    if delete_tenant(id):
        click.echo("Tenant deleted")
    else:
        click.echo("Tenant not found")

@tenant.command()
@click.argument("id", type=int)
def payments(id):
    p = get_tenant_payments(id)
    if p:
        for payment in p:
            click.echo(payment)
    else:
        click.echo("No payments or tenant not found")

@tenant.command()
@click.argument("id", type=int)
@click.option("--name", default=None)
@click.option("--phone", default=None)
@click.option("--apartment_id", type=int, default=None)
def update(id, name, phone, apartment_id):
    t = update_tenant(id, name, phone, apartment_id)
    if t:
        click.echo(f"Tenant updated: {t}")
    else:
        click.echo("Tenant not found")


# ----------------------------------------------------
# PAYMENT COMMANDS
# ----------------------------------------------------
@cli.group()
def payment():
    """Payment related commands"""
    pass

@payment.command()
@click.option("--amount", prompt="Amount", type=int)
@click.option("--date", prompt="Date (YYYY-MM-DD)")
@click.option("--tenant_id", prompt="Tenant ID", type=int)
def create(amount, date, tenant_id):
    p = create_payment(amount, date, tenant_id)
    click.echo(f"Payment added: {p}")

@payment.command()
def list():
    payments = list_payments()
    for p in payments:
        click.echo(p)

@payment.command()
@click.argument("id", type=int)
def find(id):
    p = find_payment(id)
    click.echo(p or "Payment not found")

@payment.command()
@click.argument("id", type=int)
def delete(id):
    if delete_payment(id):
        click.echo("Payment deleted")
    else:
        click.echo("Payment not found")

@payment.command()
@click.argument("id", type=int)
@click.option("--amount", type=int, default=None)
@click.option("--date_paid", default=None)
def update(id, amount, date_paid):
    p = update_payment(id, amount, date_paid)
    if p:
        click.echo(f"Payment updated: {p}")
    else:
        click.echo("Payment not found")




# ENTRY POINT

if __name__ == "__main__":
    cli()
