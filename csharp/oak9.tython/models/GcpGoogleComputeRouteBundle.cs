// <auto-generated>
//     Generated by the protocol buffer compiler.  DO NOT EDIT!
//     source: gcp/gcp_google_compute_route_bundle.proto
// </auto-generated>
#pragma warning disable 1591, 0612, 3021, 8981
#region Designer generated code

using pb = global::Google.Protobuf;
using pbc = global::Google.Protobuf.Collections;
using pbr = global::Google.Protobuf.Reflection;
using scg = global::System.Collections.Generic;
namespace Oak9.Tython.Gcp.GoogleComputeRouteBundle {

  /// <summary>Holder for reflection information generated from gcp/gcp_google_compute_route_bundle.proto</summary>
  public static partial class GcpGoogleComputeRouteBundleReflection {

    #region Descriptor
    /// <summary>File descriptor for gcp/gcp_google_compute_route_bundle.proto</summary>
    public static pbr::FileDescriptor Descriptor {
      get { return descriptor; }
    }
    private static pbr::FileDescriptor descriptor;

    static GcpGoogleComputeRouteBundleReflection() {
      byte[] descriptorData = global::System.Convert.FromBase64String(
          string.Concat(
            "CilnY3AvZ2NwX2dvb2dsZV9jb21wdXRlX3JvdXRlX2J1bmRsZS5wcm90bxIr",
            "b2FrOS50eXRob24uZ2NwLmdvb2dsZV9jb21wdXRlX3JvdXRlX2J1bmRsZRoT",
            "c2hhcmVkL3NoYXJlZC5wcm90bxobZ2NwL2djcF9jb21wdXRlX3JvdXRlLnBy",
            "b3RvIlgKEkdvb2dsZUNvbXB1dGVSb3V0ZRJCCg1jb21wdXRlX3JvdXRlGAEg",
            "ASgLMisub2FrOS50eXRob24uZ2NwLmNvbXB1dGVfcm91dGUuQ29tcHV0ZVJv",
            "dXRlYgZwcm90bzM="));
      descriptor = pbr::FileDescriptor.FromGeneratedCode(descriptorData,
          new pbr::FileDescriptor[] { global::Oak9.Tython.Shared.SharedReflection.Descriptor, global::Oak9.Tython.Gcp.ComputeRoute.GcpComputeRouteReflection.Descriptor, },
          new pbr::GeneratedClrTypeInfo(null, null, new pbr::GeneratedClrTypeInfo[] {
            new pbr::GeneratedClrTypeInfo(typeof(global::Oak9.Tython.Gcp.GoogleComputeRouteBundle.GoogleComputeRoute), global::Oak9.Tython.Gcp.GoogleComputeRouteBundle.GoogleComputeRoute.Parser, new[]{ "ComputeRoute" }, null, null, null, null)
          }));
    }
    #endregion

  }
  #region Messages
  public sealed partial class GoogleComputeRoute : pb::IMessage<GoogleComputeRoute>
  #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      , pb::IBufferMessage
  #endif
  {
    private static readonly pb::MessageParser<GoogleComputeRoute> _parser = new pb::MessageParser<GoogleComputeRoute>(() => new GoogleComputeRoute());
    private pb::UnknownFieldSet _unknownFields;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pb::MessageParser<GoogleComputeRoute> Parser { get { return _parser; } }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public static pbr::MessageDescriptor Descriptor {
      get { return global::Oak9.Tython.Gcp.GoogleComputeRouteBundle.GcpGoogleComputeRouteBundleReflection.Descriptor.MessageTypes[0]; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    pbr::MessageDescriptor pb::IMessage.Descriptor {
      get { return Descriptor; }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleComputeRoute() {
      OnConstruction();
    }

    partial void OnConstruction();

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleComputeRoute(GoogleComputeRoute other) : this() {
      computeRoute_ = other.computeRoute_ != null ? other.computeRoute_.Clone() : null;
      _unknownFields = pb::UnknownFieldSet.Clone(other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public GoogleComputeRoute Clone() {
      return new GoogleComputeRoute(this);
    }

    /// <summary>Field number for the "compute_route" field.</summary>
    public const int ComputeRouteFieldNumber = 1;
    private global::Oak9.Tython.Gcp.ComputeRoute.ComputeRoute computeRoute_;
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public global::Oak9.Tython.Gcp.ComputeRoute.ComputeRoute ComputeRoute {
      get { return computeRoute_; }
      set {
        computeRoute_ = value;
      }
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override bool Equals(object other) {
      return Equals(other as GoogleComputeRoute);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public bool Equals(GoogleComputeRoute other) {
      if (ReferenceEquals(other, null)) {
        return false;
      }
      if (ReferenceEquals(other, this)) {
        return true;
      }
      if (!object.Equals(ComputeRoute, other.ComputeRoute)) return false;
      return Equals(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override int GetHashCode() {
      int hash = 1;
      if (computeRoute_ != null) hash ^= ComputeRoute.GetHashCode();
      if (_unknownFields != null) {
        hash ^= _unknownFields.GetHashCode();
      }
      return hash;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public override string ToString() {
      return pb::JsonFormatter.ToDiagnosticString(this);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void WriteTo(pb::CodedOutputStream output) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      output.WriteRawMessage(this);
    #else
      if (computeRoute_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ComputeRoute);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(output);
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalWriteTo(ref pb::WriteContext output) {
      if (computeRoute_ != null) {
        output.WriteRawTag(10);
        output.WriteMessage(ComputeRoute);
      }
      if (_unknownFields != null) {
        _unknownFields.WriteTo(ref output);
      }
    }
    #endif

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public int CalculateSize() {
      int size = 0;
      if (computeRoute_ != null) {
        size += 1 + pb::CodedOutputStream.ComputeMessageSize(ComputeRoute);
      }
      if (_unknownFields != null) {
        size += _unknownFields.CalculateSize();
      }
      return size;
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(GoogleComputeRoute other) {
      if (other == null) {
        return;
      }
      if (other.computeRoute_ != null) {
        if (computeRoute_ == null) {
          ComputeRoute = new global::Oak9.Tython.Gcp.ComputeRoute.ComputeRoute();
        }
        ComputeRoute.MergeFrom(other.ComputeRoute);
      }
      _unknownFields = pb::UnknownFieldSet.MergeFrom(_unknownFields, other._unknownFields);
    }

    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    public void MergeFrom(pb::CodedInputStream input) {
    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
      input.ReadRawMessage(this);
    #else
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, input);
            break;
          case 10: {
            if (computeRoute_ == null) {
              ComputeRoute = new global::Oak9.Tython.Gcp.ComputeRoute.ComputeRoute();
            }
            input.ReadMessage(ComputeRoute);
            break;
          }
        }
      }
    #endif
    }

    #if !GOOGLE_PROTOBUF_REFSTRUCT_COMPATIBILITY_MODE
    [global::System.Diagnostics.DebuggerNonUserCodeAttribute]
    [global::System.CodeDom.Compiler.GeneratedCode("protoc", null)]
    void pb::IBufferMessage.InternalMergeFrom(ref pb::ParseContext input) {
      uint tag;
      while ((tag = input.ReadTag()) != 0) {
        switch(tag) {
          default:
            _unknownFields = pb::UnknownFieldSet.MergeFieldFrom(_unknownFields, ref input);
            break;
          case 10: {
            if (computeRoute_ == null) {
              ComputeRoute = new global::Oak9.Tython.Gcp.ComputeRoute.ComputeRoute();
            }
            input.ReadMessage(ComputeRoute);
            break;
          }
        }
      }
    }
    #endif

  }

  #endregion

}

#endregion Designer generated code