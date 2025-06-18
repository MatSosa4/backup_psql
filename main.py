import subprocess
import datetime
import os

# Settings
container_name = "postgres_container"
db_user = "root"
db_name = "plus"
backup_dir = "./backups"

os.makedirs(backup_dir, exist_ok=True)  # ./backups
os.makedirs(f"{backup_dir}/data", exist_ok=True)  # ./backups/data

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")

schema_file = f"{backup_dir}/schema.sql"
data_file   = f"{backup_dir}/data/{db_name}_data_{timestamp}.sql"

# Only Structure
command_schema = [
  "docker", "exec", "-t", container_name,
  "pg_dump", "-U", db_user, db_name,
  "--schema-only"
]

# Only Data
command_data = [
  "docker", "exec", "-t", container_name,
  "pg_dump", "-U", db_user, db_name,
  "--data-only"
]

# Run schema dump only if the schema structure doesnt exists
if not os.path.isfile(schema_file):
  try:
    with open(schema_file, "w") as f:
      subprocess.run(command_schema, stdout=f, check=True)
    print(f"Schema backup saved to: {schema_file}")
  except subprocess.CalledProcessError as e:
    print(f"Schema backup failed: {e}")
else:
  print("Schema already exists. Skipping.")

try:
  with open(data_file, "w") as f:
    subprocess.run(command_data, stdout=f, check=True)
  print(f"Data backup saved to: {data_file}")
except subprocess.CalledProcessError as e:
  print(f"Data backup failed: {e}")
