import scanFunc
import argparse

def main():
    parser = argparse.ArgumentParser(description="Range based PortScanner script. Initial/Final addresses are required. Scanning speed is optional (default -> 2nd level)")
    
    
    parser.add_argument("InitialIP", help="First IP in the range")
    parser.add_argument("FinalIP", help="Last IP in the range")
    parser.add_argument(
        "--sS", 
        type=int, 
        choices=[1, 2, 3], 
        default=2, 
        help="Three levels of scanning speed (1,2,3)",
        required=False
    )
    
    args = parser.parse_args()
    scanFunc.scanning(args.InitialIP,args.FinalIP,args.sS)

if __name__ == "__main__":
    main()