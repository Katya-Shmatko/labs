import typer
from typing import List, Optional
app = typer.Typer()

@app.command()
def main(numbers: List[int] = typer.Argument(None),
         input_file: Optional[str] = typer.Option(None, "-f"),
         output_file: Optional[str] = typer.Option(None, "-o")):
    if numbers:
        result = sum(numbers)
    else:
        result = 0

    if input_file:
        with open(input_file,"r") as f:
            for line in f:
                for word in line.split():
                    result += int(word)

    if output_file: 
        with open(output_file, "w") as f:
            f.write(str(result))
    else:
        print(result)

if __name__ == "__main__":
    app()