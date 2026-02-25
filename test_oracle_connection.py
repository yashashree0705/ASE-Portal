import oracledb
import os
from dotenv import load_dotenv

load_dotenv()

ORACLE_USER = os.getenv("ORACLE_USER")
ORACLE_PASSWORD = os.getenv("ORACLE_PASSWORD") 
ORACLE_DSN = os.getenv("ORACLE_CONNECT_STRING")
ORACLE_CLIENT_LIB_DIR = os.getenv("ORACLE_CLIENT_LIB_DIR")

def main():
    print("Connecting to Oracle DEV (Thick Mode)...")
    
    try:
        # Initialize thick mode
        if ORACLE_CLIENT_LIB_DIR:
            print(f"Using Instant Client: {ORACLE_CLIENT_LIB_DIR}")
            oracledb.init_oracle_client(lib_dir=ORACLE_CLIENT_LIB_DIR)
        
        # Connect
        conn = oracledb.connect(
            user=ORACLE_USER, 
            password=ORACLE_PASSWORD, 
            dsn=ORACLE_DSN
        )             
        
        cursor = conn.cursor()
        # Test ASE table access
        cursor.execute("SELECT SALESREP_NUMBER, RESOURCE_NAME FROM CUS.AWL_ASE_VIEW WHERE ROWNUM <= 5")
        rows = cursor.fetchall()
        
        print("CONNECTION SUCCESS!")
        print("ASE View sample data:")
        for row in rows:
            print(f"  ManCode: {row[0]}, Name: {row[1]}")
        
        cursor.close()
        conn.close()
        print("Done.")
        
    except Exception as e:
        print(f"Connection failed: {e}")
        return False
    
    return True

if __name__ == "__main__":
    main()
