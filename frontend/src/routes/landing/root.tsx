import { Navigate, Outlet } from "react-router-dom";
import { Navbar } from "./_components/navbar";
import { Toaster } from "sonner";
import { useSEO } from "@/hooks/useSEO";
import { isAdminRole } from "@/lib/roles";
import { useAuthStore } from "@/stores/auth-store";

export const LandingRoot = () => {
  const { isLoggedIn, role } = useAuthStore();
  useSEO("TodoApp");

  if (isLoggedIn) {
    return <Navigate to={isAdminRole(role) ? "/admin" : "/dashboard"} />;
  }

  return (
    <>
      <Navbar />
      <main className="mt-16 bg-muted/50 min-h-[calc(100vh-4rem)]">
        <Outlet />
      </main>
      <Toaster position="top-center" richColors />
    </>
  );
};
