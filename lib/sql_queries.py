select_all_female_bears_return_name_and_age = """
    select name, age from bears where sex = "F";
"""

select_all_bears_names_and_orders_in_alphabetical_order = """
    select name from bears order by name asc;
"""

select_all_bears_names_and_ages_that_are_alive_and_order_youngest_to_oldest = """
    select name, age from bears where alive = true order by age asc;
"""

select_oldest_bear_and_returns_name_and_age = """
    select name, age from bears order by age desc limit 1;
"""
select_youngest_bear_and_returns_name_and_age = """
    select name, age from bears order by age asc limit 1;
"""