from supabase import create_client, Client
import os

SUPABASE_URL = os.getenv("SUPABASE_URL") or "https://fyxvkustmfelhvseentt.supabase.co"
SUPABASE_KEY = os.getenv("SUPABASE_KEY") or "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImZ5eHZrdXN0bWZlbGh2c2VlbnR0Iiwicm9sZSI6InNlcnZpY2Vfcm9sZSIsImlhdCI6MTc2MTI4MTYyNywiZXhwIjoyMDc2ODU3NjI3fQ.3p7248sPdRG-YuFdCHSYs1Je1m9DCh_7Zr8nsiecPlA"

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)
