if m.status == GRB.OPTIMAL:
    print("✅ Optimization successful.")
    print("🔢 Objective Value (Total Cost):", m.ObjVal)
    print("\n📋 Non-zero variable values:\n")