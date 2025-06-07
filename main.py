# main.py
from scanner import scan_host
from ai_integration import analyze_scan_result

def main():
    target = input("Enter IP or Host to scan: ")
    print("\nStarting scan...\n")
    scan_output = scan_host(target)
    print(scan_output)
    
    print("\nAnalyzing results with AI...\n")
    ai_report = analyze_scan_result(scan_output)
    print(ai_report)

if __name__ == "__main__":
    main()
