import os

def removeCredentials():
  for root, _, files in os.walk("."):
    for file in files:
      if file.endswith(".prf"):
        print(f"Found - {file}")
        prf = open(os.path.join(root, file), "r")
        lines = prf.readlines()
        newLines = []

        for line in lines:
          if not ("LastSession	realname" in line or \
              "LastSession	password" in line or \
              "LastSession	certificate" in line or \
              "LastSession	callsign" in line):
                newLines.append(line);
               
        prfWrite = open(os.path.join(root, file), "w")
        for line in newLines:
          prfWrite.write(line)

        prf.close()
  print("Done! ✅")

if __name__ == "__main__":
  removeCredentials()