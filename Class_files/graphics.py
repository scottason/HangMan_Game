# case and switch for the graphic displayed

def display_hangman(tries):
    switcher = {
        0: """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / \\
                    -
            """,
        1: """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      / 
                    -
    """,
        2: """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      
                    -
    """,
        3: """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       
                    |      
                    -
    """,
        4: """
                    --------
                    |       |
                    |       O
                    |      \\|
                    |       
                    |      
                    -
    """,
        5: """
                    --------
                    |       |
                    |       O
                    |       |
                    |       
                    |      
                    -
    """,
        6: """
                    --------
                    |       |
                    |       O
                    |      
                    |       
                    |      
                    -
    """

    }
    default = """
                    --------
                    |       |
                    |       
                    |      
                    |       
                    |      
                    -
    """
    return (switcher.get(tries, """
                    --------
                    |       |
                    |       O
                    |      \\|/
                    |       |
                    |      
                    -
    """))