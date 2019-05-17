import click


import brewery

@click.command()
@click.option("--debug",default=1,help="Debug level")
@click.argument("inputfile", type=click.File('rb') )
def control(debug,inputfile):
    print("Control")
    print(str(debug))



if __name__ == "__main__":
    control()