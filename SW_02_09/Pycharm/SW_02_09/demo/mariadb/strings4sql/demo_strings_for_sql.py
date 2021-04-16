#!/usr/bin/env python3


def main():
    print("1)", "~" * 50)
    print(
        """
        foo
        bar
        demo='gugus'
        """)

    print("2)", "~" * 50)
    print(
        "foo "
        "bar "
        "demo='gugus' "
    )

    print("3)", "~" * 50)
    print(
        "foo"
        "bar"
        "demo='gugus'"
    )

    print("4)", "~" * 50)
    sql = """
    foo
    bar
    demo='gugus'
    """

    print(sql)

    print("5)", "~" * 50)
    sql = """
foo
bar
demo='gugus'
    """

    print(sql)

    print("6)", "~" * 50)
    sql = (
        "foo "
        "bar "
        "demo='gugus' "
    )

    print(sql)


if __name__ == "__main__":
    main()
